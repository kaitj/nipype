# Copyright (c) 2016, The developers of the Stanford CRN
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of crn_base nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

FROM nipype/testnipypedata
MAINTAINER Stanford Center for Reproducible Neuroscience <crn.poldracklab@gmail.com>

# Preparations
RUN ln -snf /bin/bash /bin/sh
WORKDIR /root

# Install graphviz to provide dot
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y graphviz && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p .nipype && \
    echo '[logging]' > .nipype/nipype.cfg && \
    echo 'workflow_level = DEBUG' >> .nipype/nipype.cfg && \
    echo 'interface_level = DEBUG' >> .nipype/nipype.cfg && \
    echo 'filemanip_level = DEBUG' >> .nipype/nipype.cfg

# Install this branch's code
WORKDIR /root/src
ADD . nipype/

# Install the checked out version of nipype, check that requirements are
# installed and install it for each of the three environments.
# Additionally, install matplotlib and sphinx to build documentation
RUN cd nipype/ && \
    source activate nipypetests-2.7 && \
    pip install matplotlib sphinx coverage && \
    pip install -r requirements.txt && \
    pip install -e .

RUN cd nipype/ && \
    source activate nipypetests-3.4 && \
    pip install matplotlib sphinx coverage && \
    pip install -r requirements.txt && \
    pip install -e .

RUN cd nipype/ && \
    source activate nipypetests-3.5 && \
    pip install matplotlib sphinx coverage && \
    pip install -r requirements.txt && \
    pip install -e .

WORKDIR /scratch

# Install entrypoints
ADD docker/circleci/run_* /usr/bin/
RUN chmod +x /usr/bin/run_*

# RUN echo 'source /etc/profile.d/nipype_tests.sh' >> /etc/bash.bashrc
ENTRYPOINT ["/usr/bin/run_examples.sh"]
CMD ["--help"]


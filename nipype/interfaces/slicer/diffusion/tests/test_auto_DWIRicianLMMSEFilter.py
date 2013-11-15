# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.diffusion.diffusion import DWIRicianLMMSEFilter
def test_DWIRicianLMMSEFilter_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    outputVolume=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    minnstd=dict(argstr='--minnstd %d',
    ),
    maxnstd=dict(argstr='--maxnstd %d',
    ),
    mnvf=dict(argstr='--mnvf %d',
    ),
    mnve=dict(argstr='--mnve %d',
    ),
    args=dict(argstr='%s',
    ),
    iter=dict(argstr='--iter %d',
    ),
    uav=dict(argstr='--uav ',
    ),
    re=dict(argstr='--re %s',
    sep=',',
    ),
    rf=dict(argstr='--rf %s',
    sep=',',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    compressOutput=dict(argstr='--compressOutput ',
    ),
    inputVolume=dict(position=-2,
    argstr='%s',
    ),
    hrf=dict(argstr='--hrf %f',
    ),
    )
    inputs = DWIRicianLMMSEFilter.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_DWIRicianLMMSEFilter_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = DWIRicianLMMSEFilter.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

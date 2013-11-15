# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.utils import PlotMotionParams
def test_PlotMotionParams_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    plot_type=dict(mandatory=True,
    argstr='%s',
    ),
    plot_size=dict(argstr='%s',
    ),
    out_file=dict(argstr='-o %s',
    hash_files=False,
    genfile=True,
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=1,
    mandatory=True,
    argstr='%s',
    ),
    output_type=dict(),
    in_source=dict(mandatory=True,
    ),
    )
    inputs = PlotMotionParams.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_PlotMotionParams_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = PlotMotionParams.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

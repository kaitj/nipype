# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.segmentation.simpleregiongrowingsegmentation import SimpleRegionGrowingSegmentation
def test_SimpleRegionGrowingSegmentation_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    outputVolume=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    neighborhood=dict(argstr='--neighborhood %d',
    ),
    timestep=dict(argstr='--timestep %f',
    ),
    args=dict(argstr='%s',
    ),
    labelvalue=dict(argstr='--labelvalue %d',
    ),
    smoothingIterations=dict(argstr='--smoothingIterations %d',
    ),
    seed=dict(argstr='--seed %s...',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    iterations=dict(argstr='--iterations %d',
    ),
    multiplier=dict(argstr='--multiplier %f',
    ),
    inputVolume=dict(position=-2,
    argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = SimpleRegionGrowingSegmentation.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_SimpleRegionGrowingSegmentation_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = SimpleRegionGrowingSegmentation.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

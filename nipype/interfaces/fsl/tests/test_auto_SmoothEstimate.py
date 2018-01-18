# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import SmoothEstimate


def test_SmoothEstimate_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        dof=dict(
            argstr='--dof=%d',
            mandatory=True,
            xor=['zstat_file'],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        mask_file=dict(
            argstr='--mask=%s',
            mandatory=True,
        ),
        output_type=dict(),
        residual_fit_file=dict(
            argstr='--res=%s',
            requires=['dof'],
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        zstat_file=dict(
            argstr='--zstat=%s',
            xor=['dof'],
        ),
    )
    inputs = SmoothEstimate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SmoothEstimate_outputs():
    output_map = dict(
        dlh=dict(),
        resels=dict(),
        volume=dict(),
    )
    outputs = SmoothEstimate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

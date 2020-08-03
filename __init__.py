
import os
import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty
from bpy_extras.io_utils import ImportHelper

from . panels import *
from . operators import *

bl_info = {
    "name": "project_window",
    "author": "Matt Hall",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}


classes = (
    PW_PT_Panel,
    PW_PT_CurrentProjectPanel,
    PW_PT_PrimaryProjectLocationPanel,
    PW_NewProjectOperator,
    PW_OpenProjectOperator,
    PW_NewProjectPopupOperator,
    PropertyAsGroup,
)


def register():
    """ Register all classes """
    print("LOADING")

    for c in classes:
        try:
            bpy.utils.register_class(c)
        except RuntimeError:
            print(RuntimeError)

    bpy.types.Scene.project_window = bpy.props.PointerProperty(
        type=PropertyAsGroup)


def unregister():
    """ Unregister all classes """
    print("UNLOADING")
    for c in classes:
        try:
            bpy.utils.unregister_class(c)
        except RuntimeError:
            print(RuntimeError)

    # bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

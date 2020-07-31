
import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator, Panel
import os
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


class PW_NewProjectOperator(Operator):
    bl_idname = "project_window.new_project"
    bl_label = "New Project"
    bl_options = {'REGISTER', 'UNDO'}

    # this is needed to check if the operator can be executed/invoked
    # in the current context, useful for some but not for this example
    @classmethod
    def poll(cls, context):
        # check the context here
        return context.object is not None

    def execute(self, context):
        print("New Project Pressed")
        return {'FINISHED'}


class PW_OpenProjectOperator(Operator):
    bl_idname = "project_window.open_project"
    bl_label = "Open Project"
    bl_options = {'REGISTER', 'UNDO'}

    # Define this to tell 'fileselect_add' that we want a directoy
    directory = bpy.props.StringProperty(
        name="Outdir Path",
        description="Where I will save my stuff"
        # subtype='DIR_PATH' is not needed to specify the selection mode.
        # But this will be anyway a directory path.
    )
    filter_folder = bpy.props.BoolProperty(default=True, options={'HIDDEN'})

    # this is needed to check if the operator can be executed/invoked
    # in the current context, useful for some but not for this example
    @classmethod
    def poll(cls, context):
        # check the context here
        return context.object is not None

    def execute(self, context):

        print("Selected dir: '" + self.directory + "'")
        # this is a report, it pops up in the area defined in the word
        # in curly braces {} which is the first argument, second is the actual displayed text
        self.report({'INFO'}, "Project opened successfully: " + self.directory)
        # return value tells blender wether the operation finished sueccessfully
        # needs to be in curly braces also {}
        return {'FINISHED'}

    def invoke(self, context, event):
        # Open browser, take reference to 'self' read the path to selected
        # file, put path in predetermined self fields.
        # See: https://docs.blender.org/api/current/bpy.types.WindowManager.html#bpy.types.WindowManager.fileselect_add
        context.window_manager.fileselect_add(self)
        # Tells Blender to hang on for the slow user input
        return {'RUNNING_MODAL'}


class PW_PT_Panel(Panel):
    bl_idname = "PW_PT_Panel"
    bl_label = "Project Window"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Project"

    def draw(self, context):
        # self.layout.operator("mesh.add_cube_sample",
        #                      icon='MESH_CUBE', text="Add Cube 3")
        # self.layout.label(text="Current Project")

        # layout = self.layout
        # rd = context.scene.render
        # layout.prop(rd, "filepath", text="")

        # # Current Project
        # layout.label(text="New Project:")
        # layout.operator("pw.new_project")

        pass


class PW_PT_PrimaryProjectLocationPanel(Panel):
    bl_parent_id = "PW_PT_Panel"
    bl_idname = "PW_PT_PrimaryProjectLocationPanel"
    bl_label = "Primary Project Locations"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        rd = context.scene.render
        layout.label(text="Scenes")
        layout.prop(rd, "filepath", text="")
        layout.label(text="Textures")
        layout.prop(rd, "filepath", text="")
        layout.label(text="Renders")
        layout.prop(rd, "filepath", text="")
        layout.label(text="Reference")
        layout.prop(rd, "filepath", text="")
        layout.label(text="Cache")
        layout.prop(rd, "filepath", text="")
        layout.label(text="Sound")
        layout.prop(rd, "filepath", text="")


class PW_PT_CurrentProjectPanel(Panel):
    bl_parent_id = "PW_PT_Panel"
    bl_idname = "PW_PT_CurrentProjectPanel"
    bl_label = "Current Project"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        rd = context.scene.render
        layout.label(text="Current")
        layout.prop(rd, "filepath", text="")
        scene = context.scene

        # Carver Target
        row = layout.row()

        # New row
        row = layout.row()

        # Bool diff button
        row = layout.row()
        row.operator('project_window.new_project',
                     text='New Project', icon='ADD')
        row = layout.row()
        row.operator('project_window.open_project',
                     text='Open Project', icon='FILEBROWSER')


class addCubeSample(bpy.types.Operator):
    bl_idname = 'mesh.add_cube_sample'
    bl_label = 'Add Cube'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        return {"FINISHED"}


classes = (
    PW_PT_Panel,
    PW_PT_CurrentProjectPanel,
    PW_PT_PrimaryProjectLocationPanel,
    PW_NewProjectOperator,
    PW_OpenProjectOperator
)


def register():
    print("LOADING")
    for c in classes:
        try:
            bpy.utils.register_class(c)
        except RuntimeError:
            print(RuntimeError)


def unregister():
    print("UNLOADING")
    for c in classes:
        try:
            bpy.utils.unregister_class(c)
        except RuntimeError:
            print(RuntimeError)

    # bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

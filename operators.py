import bpy
from bpy.types import Operator

from . core import Project


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
        # in curly braces {} which is the first argument, second is the actual
        # displayed text

        project = Project(self.directory)

        if project.validate():
            # TODO: set some sort of state so different file dialogs open to the
            # places specified by the project
            self.report(
                {'INFO'}, "Project opened successfully: " + self.directory)
        else:
            self.report(
                {'WARNING'}, "Project appears to be missing some folders: " + self.directory)

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
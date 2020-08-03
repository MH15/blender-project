import bpy
from bpy.types import Operator

from . core import Project
from . state import STATE
import os


class PW_NewProjectOperator(Operator):
    bl_idname = "project_window.new_project"
    bl_label = "New Project"
    bl_options = {'REGISTER', 'UNDO'}

    # The name of the new project
    name = bpy.props.StringProperty(
        name="Project Name",
        description="The name of the project folder to create"
    )

    # this is needed to check if the operator can be executed/invoked
    # in the current context, useful for some but not for this example
    @classmethod
    def poll(cls, context):
        # check the context here
        return context.object is not None

    def execute(self, context):
        print("New Project Pressed")
        bpy.ops.project_window.new_project_popup("INVOKE_DEFAULT")

        return {'FINISHED'}

    # def invoke(self, context, event):
    #     pass


class PW_NewProjectPopupOperator(Operator):
    bl_idname = "project_window.new_project_popup"
    bl_label = "New Project"
    bl_options = {'REGISTER', 'UNDO'}

    # The name of the new project
    name = bpy.props.StringProperty(
        name="Project Name",
        description="The name of the project folder to create"
    )

    # this is needed to check if the operator can be executed/invoked
    # in the current context, useful for some but not for this example
    @classmethod
    def poll(cls, context):
        # check the context here
        return context.object is not None

    def execute(self, context):
        # get the root path and set the file picker to start there
        root_path = bpy.context.scene.project_window.root_path
        project_name = self.name

        project_path = os.path.join(root_path, project_name)
        if not os.path.exists(project_path):
            os.makedirs(project_path)

        new_project = Project(project_path)
        new_project.create()

        self.report(
            {'INFO'}, f"Project `{project_name} created in {root_path}`")
        STATE["project"] = new_project

        return {'FINISHED'}

    def invoke(self, context, event):
        # self.path.default = root_path
        return context.window_manager.invoke_props_dialog(self)


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

        joiner = ","
        project = Project(self.directory)
        missing = project.validate()
        if len(missing) == 0:
            # TODO: set some sort of state so different file dialogs open to the
            # places specified by the project
            self.report(
                {'INFO'}, "Project opened successfully: " + self.directory)
        else:
            self.report(
                {'WARNING'}, "Project appears to be missing some folders: " + joiner.join(missing))

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

# Core code to verify and create new projects.
import os

from . config import PATHS
import bpy


class Project:
    """ An instance of a user-created Project """

    paths = PATHS

    def __init__(self, project_path):
        """ Create a new Project at `fullpath` """
        self.project_path = project_path
        self.is_valid = False

        # if the fullpath directory contains a valid Project
        # if self.validate():
        #     self.is_valid = True
        # else:
        #     self.is_valid = False
        #     # TODO: throw exception
        #     # self.create()
        # else create a new Project in the directory

    def validate(self):
        """ Check that each directory in self.paths exists in the Project """

        missing = []

        for folder_dir_key in self.paths:
            folder_dir_val = self.paths[folder_dir_key]
            full_dir = os.path.join(self.project_path, folder_dir_val)
            if not os.path.exists(full_dir):
                missing.append(folder_dir_val)

        return missing

    def create(self):
        """ Create a folder for each of the directories in self.paths """
        failures = []

        for folder_dir_key in self.paths:
            folder_dir_val = self.paths[folder_dir_key]
            full_dir = os.path.join(self.project_path, folder_dir_val)
            if not os.path.exists(full_dir):
                os.makedirs(full_dir)
            else:
                failures.append(folder_dir_val)
        # TODO: possibly save a blender file to {project}/scenes
        # bpy.ops.wm.save_as_mainfile(filepath="D:\\pysaved2.blend")
        return failures


def set_preferences(project_path):
    """ set Filepath preferences for textures, references, etc so the
    filepickers open in the proper directory """

    # images
    bpy.context.preferences.filepaths.texture_directory = os.path.join(
        project_path, PATHS["TEXTURES"])

    # renders
    bpy.context.preferences.filepaths.render_output_directory = os.path.join(
        project_path, PATHS["RENDERS"])

    # sounds
    bpy.context.preferences.filepaths.sound_directory = os.path.join(
        project_path, PATHS["SOUNDS"])

    # TODO: scenes
    # bpy.context.preferences.filepaths = ""

    # TODO: cache
    # bpy.context.preferences.filepaths.render_output_directory = ""

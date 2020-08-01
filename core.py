# Core code to verify and create new projects.
import os

from . config import PATHS


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

        all_exist = True

        for folder_dir in self.paths:
            full_dir = os.path.join(self.project_path, folder_dir)
            if not os.path.exists(full_dir):
                all_exist = False
                break

        return all_exist
        pass

    def create(self):
        """ Create a folder for each of the directories in self.paths """
        pass

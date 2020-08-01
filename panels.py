from bpy.types import Panel


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

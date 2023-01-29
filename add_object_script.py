bl_info = {## Gives info on the addon
    "name": "Object Adder",
    "author": "JJeris",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "View3D > Tool",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh"
}

import bpy


class TestPanel(bpy.types.Panel): ##New class
    ##Identification
    bl_label = "Object Adder" ## The label and id
    bl_idname = "PT_TestPanel"
    
    ## Where to sit on the screen
    bl_space_type = "VIEW_3D" ## The space type, ie, VIEW_3D
    bl_region_type = "UI" ## Region, it being the UI
    bl_category = "NewTab" ##Categoray, ie Item, Tool, View
    
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.4
        row = layout.row() ## Adds a new line
        
        row.label(text="Add an object", icon = "CUBE")
        row = layout.row() 
        row.operator("mesh.primitive_cube_add")
        row = layout.row() 
        row.operator("mesh.primitive_uv_sphere_add")
        row = layout.row() 
        row.operator("object.text_add")
        



class PanelA(bpy.types.Panel): ##New class
    ##Identification
    bl_label = "Scaling" ## The label and id
    bl_idname = "PT_PanelA"
    
    ## Where to sit on the screen
    bl_space_type = "VIEW_3D" ## The space type, ie, VIEW_3D
    bl_region_type = "UI" ## Region, it being the UI
    bl_category = "NewTab" ##Categoray, ie Item, Tool, View
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}

    
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row() ## Adds a new line

        row.label(text="Select  option to scale", icon = "FONT_DATA")
        row = layout.row()
        row.operator ("transform.resize")
        row = layout.row()
        layout.scale_y = 1.4
        
        col = layout.column ()
        col.prop(obj, "scale")
        


class PanelB(bpy.types.Panel): ##New class
    ##Identification
    bl_label = "Specials" ## The label and id
    bl_idname = "PT_PanelB"
    
    ## Where to sit on the screen
    bl_space_type = "VIEW_3D" ## The space type, ie, VIEW_3D
    bl_region_type = "UI" ## Region, it being the UI
    bl_category = "NewTab" ##Categoray, ie Item, Tool, View
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}

    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row() ## Adds a new line
        row.label(text="Select a Special Option", icon = "COLOR_BLUE")
        
        row = layout.row()
        row.operator("object.shade_smooth", icon = "MOD_SMOOTH", text = "Set Smooth Shading")
        row = layout.row()
        row.operator("object.subdivision_set")
        row.operator("object.modifier_add")
        












 
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)    
if __name__== "__main__":
    register()
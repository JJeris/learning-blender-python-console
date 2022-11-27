bl_info = {
    "name": "Object Adder",
    "author": "JJEris",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "View3D > Tool",
    "warnings": "",
    "wiki_url": "",
    "category": "Add Mesh"
}

import bpy

class TestPanel (bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My First Addon"
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2

        row = layout.row()    
        # ROW label and its icon (ctrl+t)
        row.label(text = "Add and object", icon = "CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = "CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = "SPHERE")
        row = layout.row()
        row.operator("object.text_add", icon = "FILE_FONT")
        
#    def add_cube(self):
        

    
    
class PanelA (bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_TestPanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My First Addon"
    bl_parent_id = "PT_TestPanel"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()    
        # ROW label and its icon (ctrl+t)
        row.label(text = "Select an option to scale yout object.", icon = "FONT_DATA")
        row = layout.row()  
        row.operator("transform.resize")
        row = layout.row()
        
        layout.scale_y = 1.2
        
        col = layout.column()
        col.prop(obj, "scale")
 
    
class PanelB (bpy.types.Panel):
    bl_label = "Panel B"
    bl_idname = "PT_TestPanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My First Addon"
    bl_parent_id = "PT_TestPanel"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()    
        # ROW label and its icon (ctrl+t)
        row.label(text = "Select a Special Option", icon = "FONT_DATA")
        row = layout.row()
        row.operator("object.shade_smooth", icon = "MOD_SMOOTH", text = "Set smooth shading")
        row = layout.row() 
        row.operator("object.subdivision_set")
        row = layout.row()   
        row.operator("object.modifier_add")  

        
        
                
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    
def unregister():
    bpy.utils.unregister_class(TaestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    
if __name__ == "__main__":
    register()
    
    
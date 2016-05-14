#version 430 /* Minimum version for compute shaders */

layout ( /* "Local Work Group" size in three dimensions: */
    local_size_x = 32,
    local_size_y = 32,
    local_size_z = 1)
    in; /* Local work group size = 32*32*1=1024 "work items"*/
    //Can't exceed 1024 work items it looks like!

layout (binding = 0, rgba32f) uniform readonly image2D tex_in; /* Read only from this texture */
uniform writeonly image2D tex_out; /* Write only to this texture */

void main(){
    /* This gives the current location of the shader in the local work group: */
    vec3 LWG_pos = gl_LocalInvocationID;
    /* This gives the size of the dimensions of the local work group: */
    vec3 LWG_size = gl_WorkGroupSize;
    /* This gives the current location of the local work group in the global work group: */
    vec3 GWG_pos = gl_WorkGroupID;
    /* This gives the size of the dimensions of the global work group: */
    vec3 GWG_size = gl_NumWorkGroups;
    
    
    /* Example post processing program: */
    ivec2 texelcoord0 = ivec2(GWG_pos.xy * LWG_size.xy + LWG_pos.xy);
    vec4 pixel = imageLoad(tex_in, texelcoord0) + 0.5;
    imageStore(tex_out, texelcoord0, pixel);
    
    
}
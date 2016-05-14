#version 330

layout (location = 0) out vec4 color;

uniform sampler2D p3d_Texture0; //Normalmap (object space)
uniform samplerCube DiffusionCM01; //Diffusionmap 01
uniform samplerCube Spec128CM01; //Specularmap 01 (shininess = 128)
uniform mat4 p3d_ModelMatrix;

in VS_OUT {
    vec2 texcoord0;
    vec3 V;
} fs_in;

void main(){
    vec3 n = vec3(texture2D(p3d_Texture0, fs_in.texcoord0)*2.0 - 1.0);
    vec3 N = mat3(p3d_ModelMatrix) * vec3(n.r, -n.g, -n.b); //This is based on default baking settings in Blender 2.72
    vec4 Diffusion = textureCube(DiffusionCM01, N);
    
    vec3 R = reflect(fs_in.V, N);
    vec4 Specularity = textureCube(Spec128CM01, R);
    
    color = Specularity + Diffusion;
}

/*
    Compare the texture normals with the native normals under matrix manipulation to
    figure out proper setting in this shader and proper baking settings in Blender!
*/
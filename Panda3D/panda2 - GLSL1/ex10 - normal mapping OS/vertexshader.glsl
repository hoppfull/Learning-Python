#version 330

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelViewMatrixInverse;
uniform mat4 p3d_ModelMatrix;

in vec2 p3d_MultiTexCoord0;

out VS_OUT {
    vec2 texcoord0;
    vec3 V;
} vs_out;

void main(){
    vs_out.texcoord0 = p3d_MultiTexCoord0;
    
    vs_out.V = vec3(p3d_ModelMatrix * (p3d_Vertex - p3d_ModelViewMatrixInverse * vec4(0.0, 0.0, 0.0, 1.0))); //WORKS! why?
    
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}
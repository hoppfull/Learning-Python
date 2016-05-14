#version 330

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewProjectionMatrix;

out vec2 texcoord0;
in vec2 p3d_MultiTexCoord0;

void main(){
    texcoord0 = p3d_MultiTexCoord0;
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}
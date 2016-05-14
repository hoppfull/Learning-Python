#version 330

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewMatrix;

in vec2 p3d_MultiTexCoord0;
out vec2 texcoord0;

void main(){
    texcoord0 = p3d_MultiTexCoord0;
    gl_Position = p3d_ModelViewMatrix * p3d_Vertex;
}
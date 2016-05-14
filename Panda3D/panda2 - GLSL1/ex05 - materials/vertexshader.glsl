#version 330

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewProjectionMatrix;

//Texturing:
in vec2 p3d_MultiTexCoord0;
out vec2 mytexcoord0;

void main(){
    mytexcoord0 = p3d_MultiTexCoord0;
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}
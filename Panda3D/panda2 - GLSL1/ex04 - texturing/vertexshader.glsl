#version 330

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewProjectionMatrix;

//Texturing:
in vec2 p3d_MultiTexCoord0; //This can only be handled properly by the vertexshader
out vec2 texcoord0;         //This is used to store the texture coordinate for this vertex and send it to the fragmentshader

void main(){
    texcoord0 = p3d_MultiTexCoord0; //Copying the texture coordinate for this vertex
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}
#version 330 core

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewMatrix;

in vec2 p3d_MultiTexCoord0;
out vec2 texcoord0;

void main(){
	texcoord0.x = p3d_MultiTexCoord0.x * 800/1024;
	texcoord0.y = p3d_MultiTexCoord0.y * 600/1024;
	gl_Position = p3d_ModelViewMatrix * p3d_Vertex;
}
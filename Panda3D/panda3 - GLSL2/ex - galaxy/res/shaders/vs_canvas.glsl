#version 330 core

in vec3 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;
uniform mat4 p3d_ModelViewProjectionMatrix;

uniform vec2 win_size;
uniform vec2 buffer_size;

out vec2 texcoord0;
out vec2 texcoord1;

void main(){
	texcoord0.x = p3d_MultiTexCoord0.x * win_size.x/buffer_size.x;
	texcoord0.y = p3d_MultiTexCoord0.y * win_size.y/buffer_size.y;
	texcoord1 = p3d_MultiTexCoord0;
	gl_Position = p3d_ModelViewProjectionMatrix * vec4(p3d_Vertex*2 + vec3(-1, 0, -1), 1.0);
}
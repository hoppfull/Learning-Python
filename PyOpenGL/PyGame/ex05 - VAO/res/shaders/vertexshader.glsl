#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 uvmap0;

uniform mat4 my_ModelMatrix;
uniform mat4 my_ViewMatrix;
uniform mat4 my_ProjectionMatrix;

void main(){
	gl_Position = my_ProjectionMatrix * my_ViewMatrix * my_ModelMatrix * vec4(position, 1.0);
}
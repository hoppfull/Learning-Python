#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D tex_render;
uniform sampler2D whatevs;
in vec2 texcoord0;

void main(){
	fragColor = texture(tex_render, texcoord0);
}
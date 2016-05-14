#version 330 core

out vec4 fragColor;

uniform sampler2D p3d_Texture0;
in vec2 texcoord0;

void main(){
	fragColor = texture2D(p3d_Texture0, texcoord0);
}
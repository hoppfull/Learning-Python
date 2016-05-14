#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D tex_render;
in vec2 texcoord0;

float blur_w[4] = float[4](0.28, 0.22, 0.11, 0.03);

void main(){
	vec4 c = texture(tex_render, texcoord0) * blur_w[0];
	for(int i = 1; i < 4; i++){
		c += texture(tex_render, texcoord0 + vec2(0, 0.005)*i) * blur_w[i];
		c += texture(tex_render, texcoord0 - vec2(0, 0.005)*i) * blur_w[i];
	}
	fragColor = c;
}
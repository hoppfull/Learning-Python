#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D tex_vgauss;
in vec2 texcoord0;

float blur_w[4] = float[4](0.28, 0.22, 0.11, 0.03);

void main(){
	vec4 c = texture(tex_vgauss, texcoord0) * blur_w[0];
	for(int i = 1; i < 4; i++){
		c += texture(tex_vgauss, texcoord0 + vec2(0.005, 0)*i) * blur_w[i];
		c += texture(tex_vgauss, texcoord0 - vec2(0.005, 0)*i) * blur_w[i];
	}
	fragColor = c;
}
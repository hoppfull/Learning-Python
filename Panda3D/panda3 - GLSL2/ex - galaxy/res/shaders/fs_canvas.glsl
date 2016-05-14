#version 330 core

out vec4 fragColor;

in vec2 texcoord0;
in vec2 texcoord1;
uniform sampler2D hires_output;
uniform sampler2D lores_output;
uniform sampler2D vignette;

void main(){
	// fragColor
		// = texture(hires_output, texcoord0)
		// * texture(vignette, texcoord1)
		// + texture(lores_output, texcoord1);
	fragColor = texture(lores_output, texcoord1);
}
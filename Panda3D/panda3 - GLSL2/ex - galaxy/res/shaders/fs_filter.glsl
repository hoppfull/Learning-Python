#version 330 core

out vec4 fragColor;

in vec2 texcoord0;
in vec2 texcoord1;
uniform sampler2D hires_output;
uniform sampler2D lens_weight;

// float blur_a = 0.01; //Blur amount
// float blur_q = 5; //Blur quality

void main(){
	
	
	vec4 r = vec4(0.0);
	/* Blurring: */
	// for(int i = 0; i < blur_q; i++){
		// for(int j = 0; j < blur_q; j++){
			// r += texture(hires_output, vec2(0.75, 0.5)-(texcoord0 + vec2(
				// (i - blur_q/2) * blur_a, //Blurring in x direction
				// (j - blur_q/2) * blur_a //Blurring in y direction
				// ))) / (blur_q * blur_q);
		// }
	// }
	
	vec4 a = texture(hires_output, texcoord0);
	
	
	
	fragColor = a;
}
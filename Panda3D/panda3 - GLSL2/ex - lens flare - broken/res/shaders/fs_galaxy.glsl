#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D p3d_Texture0;
uniform sampler2D p3d_Texture1;
in vec2 texcoord0;

uniform float turn;
float swirl = 20; //Higher means more twisting in center and less on edges

mat2 rotate(in float t){
	return(mat2(
		cos(t), -sin(t),
		sin(t),  cos(t)));
}

float twist(in float t, in float s){
	return(
		mix( t*s, 0, min(1, pow(2*length( texcoord0 - vec2(0.5) ), 1/s)) )
	);
}

float blending(in float t){
	float blend = 0;
	if(t < 1 && 0.5 <= t)
		blend = 2*(1-t);
	else if(t < 0.5)
		blend = 2*t;
	return(blend);
}

void main(){
	float turn2 = 0;
	if(0 <= turn && turn < 0.5)
		turn2 = turn + 0.5;
	else if(0.5 <= turn && turn <= 1)
		turn2 = turn - 0.5;
	
	vec2 uv_1 = rotate(twist(turn, swirl)) * (texcoord0 - vec2(0.5)) + vec2(0.5);
	vec2 uv_2 = rotate(twist(turn2, swirl)) * (texcoord0 - vec2(0.5)) + vec2(0.5);
	
	float a = blending(turn);
	float b = blending(turn2);mix(vec4(0,0,0,1), texture(p3d_Texture0, uv_2), b);
	
	fragColor =
		mix(vec4(0,0,0,1), texture(p3d_Texture1, uv_1), a) +
		mix(vec4(0,0,0,1), texture(p3d_Texture1, uv_2), b) +
		texture(p3d_Texture0, texcoord0);
}
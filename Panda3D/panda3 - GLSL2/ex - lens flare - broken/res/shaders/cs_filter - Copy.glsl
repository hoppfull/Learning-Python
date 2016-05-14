#version 430 core

layout ( /* "Local Work Group" size in three dimensions: */
    local_size_x = 1,
    local_size_y = 256,
    local_size_z = 1)
    in; /* Local work group size = 1*256*1=256 "work items"*/
    //Can't exceed 1024 work items it looks like!

layout (binding = 0, rgba32f) uniform image2D lores_buffer_p;
layout (binding = 1, rgba32f) uniform image2D temp1_buffer_p;
layout (binding = 2, rgba32f) uniform image2D temp2_buffer_p;

int blur_n = 10;
int blur_d = 4;

float binomial(int n, int k){
	float nums = 1.0;
	int dens = 1;
	
	for(int i = 1; i <= k; i++){
		nums *= (n - k + i);
		dens *= i;
	}
	
	return nums/(dens * pow(2, n));
}

void main(){
	vec3 GWG_pos = gl_WorkGroupID;
	vec3 LWG_pos = gl_LocalInvocationID;

	ivec2 texel = ivec2(GWG_pos.xy + LWG_pos.xy);
	
	vec4 horizontal = imageLoad(lores_buffer_p, texel) * binomial(blur_n*2 + 2, blur_n + 1);
	for(int i = 1; i <= blur_n; i++){
		horizontal += imageLoad(lores_buffer_p, texel + ivec2( i*blur_d, 0)) * binomial(blur_n*2 + 2, blur_n + 1 - i);
		horizontal += imageLoad(lores_buffer_p, texel + ivec2(-i*blur_d, 0)) * binomial(blur_n*2 + 2, blur_n + 1 - i);
	}
	imageStore(temp1_buffer_p, texel, horizontal);
	
	barrier();
	memoryBarrierShared();
	
	vec4 vertical = imageLoad(temp1_buffer_p, texel) * binomial(blur_n*2 + 1, blur_n + 1);
	for(int i = 1; i <= blur_n; i++){
		vertical += imageLoad(temp1_buffer_p, texel + ivec2(0, i*blur_d)) * binomial(blur_n*2 + 2, blur_n + 1 - i);
		vertical += imageLoad(temp1_buffer_p, texel + ivec2(0,-i*blur_d)) * binomial(blur_n*2 + 2, blur_n + 1 - i);
	}
	imageStore(temp2_buffer_p, texel, vertical);
}
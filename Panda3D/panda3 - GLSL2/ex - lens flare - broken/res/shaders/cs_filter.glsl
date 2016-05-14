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

float blur_w[3] = {0.285, 0.43, 0.285};

void main(){
	vec3 GWG_pos = gl_WorkGroupID;
	vec3 LWG_pos = gl_LocalInvocationID;

	ivec2 texel = ivec2(GWG_pos.xy + LWG_pos.xy);
	
	vec4 gauss = vec4(0);
	for(int i = 0; i < 3; i++){
		gauss += imageLoad(lores_buffer_p, texel + ivec2(i - 1, 0)*2) * blur_w[i];
	}
	imageStore(temp1_buffer_p, texel, gauss);
	
	barrier();
	
	gauss = vec4(0);
	for(int i = 0; i < 3; i++){
		gauss += imageLoad(temp1_buffer_p, texel + ivec2(0, i - 1)*2) * blur_w[i];
	}
	imageStore(temp2_buffer_p, texel, gauss);
	/*
	memoryBarrier();
	
	gauss = vec4(0);
	for(int i = 0; i < 3; i++){
		gauss += imageLoad(temp2_buffer_p, texel.yx + ivec2(i - 1, 0)*4) * blur_w[i];
	}
	imageStore(temp1_buffer_p, texel.yx, gauss);
	*/
}
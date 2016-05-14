#version 330

layout (location = 0) out vec4 color;
uniform sampler2D p3d_Texture0;

in VS_OUT {
    vec2 texcoord0;
    vec3 V;
    vec3 L;
} fs_in;

void main(){
    vec3 N = vec3(texture2D(p3d_Texture0, fs_in.texcoord0).rgb) * 2.0 - 1.0;
    vec3 L = normalize(fs_in.L);
    vec4 Diffusion = max(0.0, dot(N, L)) * vec4(1.0);
    
    vec3 R = reflect(-L, N);
    vec3 V = normalize(fs_in.V);
    vec4 Specularity = pow(max(0.0, dot(R, V)), 32) * vec4(1.0);
    
    
    
    color = Diffusion;
}
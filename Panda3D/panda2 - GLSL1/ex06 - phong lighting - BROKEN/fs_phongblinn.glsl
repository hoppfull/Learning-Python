#version 330

layout (location = 0) out vec4 color;

in VS_OUT {
    vec3 N;
    vec3 L;
    vec3 V;
} fs_in;

uniform struct {
    vec4 ambient;
    vec4 diffuse;
    vec4 emission;
    vec3 specular;
    float shininess;
} p3d_Material;

uniform vec3 dlight1_col;
uniform vec3 Ambience;

void main(){
    //Normalize incomming N,L and V:
    vec3 N = normalize(fs_in.N);
    vec3 L = normalize(fs_in.L);
    vec3 V = normalize(fs_in.V);
    /* VERY interesting smoothing-effect if these three are normalized
    in vertexshader instead!*/
    
    //Compute reflected light ray
    vec3 H = normalize(L + V); 
    
    //Compute diffusion (lit2dark shading):
    vec3 diffusion = max(0.0, dot(N,L)) * p3d_Material.diffuse.rgb * dlight1_col;
    //Compute specularity (shininess):
    vec3 specularity = pow(max(0.0, dot(N, H)), p3d_Material.shininess) * p3d_Material.specular;
    
    color = vec4(diffusion + specularity + Ambience, 1.0);
}

/*
    This is a little less accurate but faster to calculate. Not by much but a bit.
*/
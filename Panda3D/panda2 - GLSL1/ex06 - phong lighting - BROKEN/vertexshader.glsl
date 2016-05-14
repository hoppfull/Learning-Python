#version 330

in vec4 p3d_Vertex;
in vec3 p3d_Normal;

uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelViewMatrix;
uniform mat3 p3d_NormalMatrix;

out VS_OUT { //Viewspace vectors:
    vec3 N; //Surface Normal
    vec3 L; //Surface to light
    vec3 V; //Surface to eye
} vs_out;

uniform vec4 dlight1_pos;
void main(){
    //Origin position in viewspace:
    vec4 T = p3d_ModelViewMatrix * vec4(0.0, 0.0, 0.0, 1.0);
    //Vertex position in viewspace:
    vec4 P = p3d_ModelViewMatrix * p3d_Vertex;

    //Calculate surface normal in viewspace:
    vs_out.N = p3d_NormalMatrix * p3d_Normal;
    
    //Calculate surface2light: (use P for point light, or T for directional light!)
    vs_out.L = vec3(p3d_ModelViewMatrix * dlight1_pos - T);
    
    //Calculate surface2eye:
    vs_out.V = - P.xyz;
    
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}
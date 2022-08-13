function animate() {
    requestAnimationFrame(animate);
    // landscape.rotateX(0.001);
    renderer.render(scene, camera);
}

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xFFFFFF);

const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer()
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


const width = 200;
const height = 100;
const sections = 64;
const smoothness = 100;
const depth = -1;


let terrain = new Terrain(width, height, sections, smoothness)
terrain.generate()

let points = []
for(let x = 0; x <= sections; x++) {
    for(let y = 0; y <= sections; y++) {
        points.push(new THREE.Vector3(x, y, terrain.array[x][y]))
        // groundGeometry.vertices[index].z = terrain.array[i][j] + depth;
    }
}

const geometry = new THREE.PlaneGeometry(width, height, sections, sections).setFromPoints(points);
geometry.translate(-1 * (sections / 2), -1 * (sections / 2), 0);

const material = new THREE.MeshBasicMaterial({ color: 0x000000, wireframe: true });
const landscape = new THREE.Mesh(geometry, material);

camera.position.copy(landscape.position);
camera.position.z = 100;


// scene.add(geometry)
scene.add(landscape);

animate()

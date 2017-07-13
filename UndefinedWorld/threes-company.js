<!-- https://codecombat.com/play/level/threes-company -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/85/three.min.js">
</script>
<script>
    var camera, scene, renderer;
	var mesh;
	init();
	animate();
	function init() {
		camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
		camera.position.z = 400;
		scene = new THREE.Scene();
		var texture = new THREE.TextureLoader().load( '' );
		var geometry = new THREE.BoxBufferGeometry( 200, 200, 200 );
		var material = new THREE.MeshBasicMaterial( );
		mesh = new THREE.Mesh( geometry, material );
		scene.add( mesh );
		renderer = new THREE.WebGLRenderer();
		renderer.setPixelRatio( window.devicePixelRatio );
		renderer.setSize( window.innerWidth, window.innerHeight );
		document.body.appendChild( renderer.domElement );
		//console.log("how many times")
		//
		window.addEventListener( 'resize', onWindowResize, false );
	}
	function onWindowResize() {
		camera.aspect = window.innerWidth / window.innerHeight;
		camera.updateProjectionMatrix();
		renderer.setSize( window.innerWidth, window.innerHeight );
	}
	function animate() {
		requestAnimationFrame( animate );
		mesh.rotation.x += 0.005;
		mesh.rotation.y += 0.01;
		renderer.render( scene, camera );
	}
</script>


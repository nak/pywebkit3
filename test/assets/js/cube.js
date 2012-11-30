var cameraPos = {x:0,y:0,z:100};	
var linaccel=new THREE.Vector3(0.0,0.0,0.0);
var rotaccel = new THREE.Vector3(0.0,0.0,0.0);
var rotations = [null, null, null,null,null,null];
var n = [null, null, null,null,null,null];

  

const CALIBRATED = 0;
const RAW = 1;
var accel_units_set = false;

var SCREEN_WIDTH = 250;
var SCREEN_HEIGHT = 200;

var container;

var particle;

var camera;
var scene;
var renderer;

var mouseX = 0;
var mouseY = 0;

var particles = []; 
var particleImage = new Image();//THREE.ImageUtils.loadTexture( "img/ParticleSmoke.png" );
particleImage.src = 'assets/img/ParticleSmoke.png'; 



        
function updateYPR( yaw, pitch, roll ){
 
	yaw = (Math.round(yaw*100.0))/100.0;
	pitch = (Math.round(pitch*100.0))/100.0;
	roll = (Math.round(roll*100.0))/100.0;
	pitch=-pitch;
     
	$('.cubie').each( function(index){
		// alert(index);
		if (rotations[index]==null){
            
			rotations[index] = $(this).css('-webkit-transform')  ;
            if (!rotations[index]){
              rotations[index] = $(this).css('-moz-transform');
            }
            if (!rotations[index]){
              rotations[index] = $(this).css('-ms-transform');
            }
            n[index] = eval($(this).attr('n'));
		}
          
          
		csstext = 'rotateY('+yaw+'deg) rotateX(' + (pitch) +'deg) rotateZ(' + roll +'deg) '+ rotations[index];
         
		$(this).css( '-webkit-transform',csstext);
		$(this).css( '-moz-transform',csstext);
		$(this).css( '-ms-transform',csstext);
	});
     
}



var windowHalfX ;
var windowHalfY;
	
  
$(document).ready(function(){

	windowHalfX = $('#canvas')[0].innerWidth / 2;
    windowHalfY = $('#canvas')[0].innerHeight / 2;
		         
});


function cube_init() {
	container = document.createElement('div');
	$('#canvas')[0].appendChild(container);
	$(container).width(SCREEN_WIDTH);
    $(container).height(SCREEN_HEIGHT);
    $(container).css('background-color','black');
	camera = new THREE.PerspectiveCamera( 75, 1, 1, 10000);
	camera.position.z = 1000;

	scene = new THREE.Scene();
	scene.add(camera);
		
	renderer = new THREE.CanvasRenderer();
	renderer.setSize(SCREEN_WIDTH,SCREEN_HEIGHT);
	var material = new THREE.ParticleBasicMaterial( { map: new THREE.Texture(particleImage) } );
		
	for (var i = 0; i < 500; i++) {

		particle = new Particle3D( material);
		particle.position.x = Math.random() * 2000 - 1000;
		particle.position.y = Math.random() * 2000 - 1000;
		particle.position.z = Math.random() * 2000 - 1000;
		particle.scale.x = particle.scale.y =  1;
		scene.add( particle );
		
		particles.push(particle); 
	}

	container.appendChild( renderer.domElement );


	
	/* USE THE FOLLOWING TO UNCOMMENT AND ACTIVE TEST PROGREAM*/
	enable_unit_test();
	
	//initial view:
	updateYPR(-45, 45, 45);

    $('textarea').css('font-weight','bold');
}
var py_ypr_updater;

function enable_unit_test(){
  py_ypr_updater = cube.YPR_Updater.new_( "ypr_updater",45, 45, -45);
	setInterval( test_loop, 1000 / 60 );
}


//
var YPR = [45,45,-45];
var simtime = 0.0;
var sign=1;
//Created from python and as python object too!!:

function test_loop() {
  //Python obejct accessible in javascript!!!
    py_ypr_updater.update( 0.3, sign*0.5, 0.7);
    YPR[0] = py_ypr_updater.yaw()
    YPR[1] = py_ypr_updater.pitch()
    YPR[2] = py_ypr_updater.roll()
	linaccel.x = 0.06*Math.sin(TO_RADIANS*YPR[0]);
    linaccel.y = 0.06*Math.cos(TO_RADIANS*YPR[0]);
    updateYPR(YPR[0], YPR[1], YPR[2]);
    simtime += 1.0;
    snow_loop();
}

function snow_loop(){

	for(var i = 0; i<particles.length; i++)
	{

		var particle = particles[i]; 
		particle.updatePhysics(); 

		with(particle.position)
		{
            factor=7.5;
            while(y<-factor*SCREEN_WIDTH/2) y+=factor*SCREEN_WIDTH; 
            while(y>factor*SCREEN_WIDTH/2) y -= factor*SCREEN_WIDTH;
			while(x>factor*SCREEN_WIDTH/2) x-=factor*SCREEN_WIDTH; 
			while(x<-factor*SCREEN_WIDTH/2) x+=factor*SCREEN_WIDTH; 
			if(z>100) z-=2000; 
			else if(z<-100) z+=2000;
           // x=50.0; y = 750.0; z= 0.0;
           // if(y > 750.0){ alert([x,y,z]);}
		}				
	}

	camera.position.x = cameraPos.x;//( mouseX - camera.position.x ) * 0.05;
    camera.position.y = cameraPos.y;//( - mouseY - camera.position.y ) * 0.05;
    camera.position.z = cameraPos.z;
    camera.lookAt(scene.position); 
	renderer.render( scene, camera );

	
}

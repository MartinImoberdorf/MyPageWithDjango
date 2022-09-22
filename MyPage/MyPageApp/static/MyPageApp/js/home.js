//MAQUINA DE ESCRIBIR EFECTO

const typed = new Typed('.Typed',{
    strings:[
        '<b class="idiomas">HELLO</b>',
        '<b class="idiomas">BIENVENIDO</b>',
        '<b class="idiomas">歡迎</b>',
        '<b class="idiomas">BENVINGUT</b>',
        '<b class="idiomas">ようこそ</b>',
        '<b class="idiomas">BIENVENUE</b>',
        '<b class="idiomas">WELKOM</b>',
        '<b class="idiomas">BENVENUTA</b>',
    ],

	typeSpeed: 50, // Velocidad en mlisegundos para poner una letra,
	startDelay: 500, // Tiempo de retraso en iniciar la animacion. Aplica tambien cuando termina y vuelve a iniciar,
	backSpeed: 100, // Velocidad en milisegundos para borrrar una letra,
	shuffle: false, // Alterar el orden en el que escribe las palabras.
	backDelay: 1500, // Tiempo de espera despues de que termina de escribir una palabra.
	loop: true, // Repetir el array de strings
	loopCount: false, // Cantidad de veces a repetir el array.  false = infinite
	showCursor: true, // Mostrar cursor palpitanto
	cursorChar: '|', // Caracter para el cursor
	contentType: 'html', // 'html' o 'null' para texto sin formato
});
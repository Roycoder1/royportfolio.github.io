
const welcome = document.getElementById("welcome");

const welcText = 'Welcome!';

for (let i = 0; i < welcText.length; i++) {
    setTimeout(() => {
        
        welcome.innerText += welcText[i];
    }, i * 100);
    
}

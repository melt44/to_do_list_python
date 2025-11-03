document.addEventListener('DOMContentLoaded', function() {
    console.log("Jumpscare Script Loading Confirmed.");
    
    const jumpscareFnafImage = document.getElementById('fnaf-susto');
    const jumpscareFlamengoImage = document.getElementById('mengo-susto'); 
    const jumpscareSound = document.getElementById('jumpscare-sound');
    
    const updateForms = document.querySelectorAll('form[action$="/update"]'); 

    // Duração
    const totalDuration = 7000; 
    const transitionTime = 700; 
    
    updateForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            
            const submitter = event.submitter; 
            if (!submitter || submitter.value !== 'X') {
                return; 
            }
            
            event.preventDefault(); 
            
            if (!jumpscareFnafImage || !jumpscareFlamengoImage) {
                 this.submit(); 
                 return;
            }

            // 1. Mostra o FNaF
            jumpscareFnafImage.classList.add('active');
            
            // Toca o som 
            if (jumpscareSound) {
                jumpscareSound.currentTime = -0.5; 
                jumpscareSound.play().catch(e => {
                     console.warn("Áudio bloqueado.", e);
                }); 
            }

            setTimeout(() => {
                jumpscareFnafImage.classList.remove('active'); // Esconde FNaF
                jumpscareFlamengoImage.classList.add('active'); // Mostra Flamengo
            }, transitionTime);
            
            setTimeout(() => {
                jumpscareFlamengoImage.classList.remove('active'); // Esconde Flamengo
                
                // É um campo temporário pro Flask não exibir Bad Request
                const tempInput = document.createElement('input');
                tempInput.type = 'hidden';
                tempInput.name = submitter.name; 
                tempInput.value = submitter.value; 
                form.appendChild(tempInput); 
                
                form.submit(); // Submete o formulário
            }, totalDuration);
        });
    });
});
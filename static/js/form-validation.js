document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('attendance-form');
    const submitButton = form.querySelector('input[type="submit"]');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', function (event) {
        let isValid = true;
        errorMessage.textContent = '';

        // Para1 bo'yicha tekshirish
        const para1Selects = form.querySelectorAll('select[name^="para1_"]');
        const para2Selects = form.querySelectorAll('select[name^="para2_"]');
        const para3Selects = form.querySelectorAll('select[name^="para3_"]');

        if (Array.from(para1Selects).some(select => select.disabled === false && select.value === '')) {
            isValid = false;
            errorMessage.textContent += 'Barcha "1 - Para" tanlovlarini to\'ldiring.\n';
        }

        if (Array.from(para2Selects).some(select => select.disabled === false && select.value === '')) {
            isValid = false;
            errorMessage.textContent += 'Barcha "2 - Para" tanlovlarini to\'ldiring.\n';
        }

        if (Array.from(para3Selects).some(select => select.disabled === false && select.value === '')) {
            isValid = false;
            errorMessage.textContent += 'Barcha "3 - Para" tanlovlarini to\'ldiring.\n';
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});

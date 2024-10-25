function formatCardNumber(cardNumber) {
    const digits = cardNumber.replace(/\D/g, '');
    return digits.replace(/(.{4})/g, '$1 ').trim();
}
const cardElements = document.querySelectorAll('[data-target-copy]');

cardElements.forEach(element => {
    const cardNumber = element.textContent || element.innerText;
    const formattedNumber = formatCardNumber(cardNumber);
    element.textContent = formattedNumber;
});

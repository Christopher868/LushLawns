document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("searchInput").addEventListener("keyup", filterPartsResults);
});

function filterPartsResults() {
    let input = document.getElementById('filter-parts').value.toLowerCase();
    let items = document.querySelectorAll('.part-item');

    items.forEach(item => {
        let partNumber = item.querySelector('.part_number');
        let partItem = partNumber.textContent.toLowerCase();
        item.style.display = partItem.includes(input) ? "grid" : 'none';
    });
}
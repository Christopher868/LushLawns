document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("searchInput").addEventListener("keyup", filterModelResults);
});

function filterModelResults() {
    let input = document.getElementById('filter-models').value.toLowerCase();
    let items = document.querySelectorAll('.model-item');

    items.forEach(item => {
        let modelNumber = item.querySelector('.model_number');
        let modelItem = modelNumber.textContent.toLowerCase();
        item.style.display = modelItem.includes(input) ? "grid" : 'none';
    });
}
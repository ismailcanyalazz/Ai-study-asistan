// API Configuration
const API_URL = 'http://localhost:8000';

// Utility Functions
function showLoading(buttonId) {
    const button = document.getElementById(buttonId);
    button.disabled = true;
    const originalText = button.innerHTML;
    button.setAttribute('data-original-text', originalText);
    button.innerHTML = '<span class="loading"></span> İşleniyor...';
}

function hideLoading(buttonId) {
    const button = document.getElementById(buttonId);
    const originalText = button.getAttribute('data-original-text');
    button.disabled = false;
    button.innerHTML = originalText;
}

// Yan Panel Sistemi
function openResultPanel(title, content, icon = '✨') {
    // Panel varsa kapat
    closeResultPanel();

    // Yeni panel oluştur
    const panel = document.createElement('div');
    panel.className = 'result-panel';
    panel.id = 'result-panel';

    panel.innerHTML = `
        <div class="result-panel-overlay" onclick="closeResultPanel()"></div>
        <div class="result-panel-content">
            <div class="result-panel-header">
                <div class="result-panel-title">
                    <span class="result-panel-icon">${icon}</span>
                    <h2>${title}</h2>
                </div>
                <button class="result-panel-close" onclick="closeResultPanel()">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
            <div class="result-panel-body">
                ${formatContent(content)}
            </div>
            <div class="result-panel-footer">
                <button class="btn-copy" onclick="copyToClipboard()">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Kopyala
                </button>
                <button class="btn-close-panel" onclick="closeResultPanel()">Kapat</button>
            </div>
        </div>
    `;

    document.body.appendChild(panel);

    // Animasyon için timeout
    setTimeout(() => {
        panel.classList.add('active');
    }, 10);
}

function closeResultPanel() {
    const panel = document.getElementById('result-panel');
    if (panel) {
        panel.classList.remove('active');
        setTimeout(() => {
            panel.remove();
        }, 300);
    }
}

function formatContent(content) {
    // Markdown-style formatting
    let formatted = content
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/###\s(.*?)(\n|$)/g, '<h3>$1</h3>')
        .replace(/##\s(.*?)(\n|$)/g, '<h2>$1</h2>')
        .replace(/---/g, '<hr>')
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>');

    return `<p>${formatted}</p>`;
}

function copyToClipboard() {
    const content = document.querySelector('.result-panel-body').innerText;
    navigator.clipboard.writeText(content).then(() => {
        const btn = document.querySelector('.btn-copy');
        const originalText = btn.innerHTML;
        btn.innerHTML = `
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            Kopyalandı!
        `;
        btn.style.background = 'var(--gradient-success)';

        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.style.background = '';
        }, 2000);
    });
}

function showError(message, icon = '❌') {
    openResultPanel('Hata', `<div class="error-message">${message}</div>`, icon);
}

// API Call Function
async function callAPI(endpoint, data) {
    const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Bir hata oluştu');
    }

    return await response.json();
}

// 1. Konu Özetleme
async function konuOzetle() {
    const konu = document.getElementById('konu-input').value.trim();

    if (!konu) {
        showError('Lütfen bir konu girin');
        return;
    }

    showLoading('ozet-btn');

    try {
        const result = await callAPI('/ozet', { konu });
        openResultPanel('📝 Konu Özeti', result.ozet, '📝');
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading('ozet-btn');
    }
}

// 2. Soru Üretme
async function soruUret() {
    const konu = document.getElementById('soru-konu-input').value.trim();

    if (!konu) {
        showError('Lütfen bir konu girin');
        return;
    }

    showLoading('soru-btn');

    try {
        const result = await callAPI('/soru-uret', { konu });
        openResultPanel('❓ Üretilen Sorular', result.sorular, '❓');
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading('soru-btn');
    }
}

// 3. Çalışma Planı
async function calismaPlanOlustur() {
    const konu = document.getElementById('plan-konu-input').value.trim();
    const seviye = document.getElementById('seviye-select').value;
    const sure = document.getElementById('sure-input').value.trim();
    const gun = document.getElementById('gun-input').value.trim();

    if (!konu || !sure || !gun) {
        showError('Lütfen tüm alanları doldurun');
        return;
    }

    showLoading('plan-btn');

    try {
        const result = await callAPI('/calisma-plani', { konu, seviye, sure, gun });
        openResultPanel('📅 Çalışma Planınız', result.plan, '📅');
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading('plan-btn');
    }
}

// 4. Metin Açıklama
async function metinAcikla() {
    const metin = document.getElementById('metin-input').value.trim();

    if (!metin) {
        showError('Lütfen bir metin girin');
        return;
    }

    showLoading('metin-btn');

    try {
        const result = await callAPI('/metin-acikla', { metin });
        openResultPanel('💡 Metin Açıklaması', result.aciklama, '💡');
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading('metin-btn');
    }
}

// 5. PDF Upload
async function pdfYukle() {
    const fileInput = document.getElementById('pdf-input');
    const file = fileInput.files[0];

    if (!file) {
        showError('Lütfen bir PDF dosyası seçin');
        return;
    }

    showLoading('pdf-btn');

    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${API_URL}/pdf-yukle`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'PDF yükleme hatası');
        }

        const result = await response.json();
        openResultPanel(`📄 ${result.dosya_adi}`, result.aciklama, '📄');
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading('pdf-btn');
    }
}

// File input label update
document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('pdf-input');
    const fileLabel = document.querySelector('.file-upload-label span');

    if (fileInput && fileLabel) {
        fileInput.addEventListener('change', (e) => {
            const fileName = e.target.files[0]?.name || 'PDF dosyası seçin';
            fileLabel.textContent = fileName;
        });
    }

    // Enter key support for inputs
    document.querySelectorAll('input, textarea').forEach(input => {
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey && input.tagName !== 'TEXTAREA') {
                e.preventDefault();
                const card = input.closest('.card');
                const button = card?.querySelector('button');
                if (button) button.click();
            }
        });
    });

    // ESC key to close panel
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeResultPanel();
        }
    });
});

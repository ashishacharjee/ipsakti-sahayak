import codecs
import os

with codecs.open('app/static/terms.html', 'r', 'utf-8') as f:
    template = f.read()

# Remove sidebar and make it a single column centered layout for these pages
import re
# Strip the <aside> entirely
template = re.sub(r'<aside.*?</aside>', '', template, flags=re.DOTALL)
# Change the main flex layout
template = template.replace('flex-col md:flex-row gap-12 md:gap-20', 'flex-col max-w-4xl mx-auto')

def make_page(filename, title, content_html):
    html = template
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | IP-SAKTI Sahayak</title>', html)
    html = re.sub(r'<h1.*?>.*?</h1>', f'<h1 class="text-4xl md:text-5xl font-bold text-vedic-forest tracking-tight mb-4">{title}</h1>', html)
    
    # Replace article content
    article_content = f'''<div class="border-b border-vedic-border pb-8">
                <h1 class="text-4xl md:text-5xl font-bold text-vedic-forest tracking-tight mb-4">{title}</h1>
                <p class="text-vedic-textSecondary">Last updated: September 2026</p>
            </div>
            
            <section class="term-section">
                <div class="prose max-w-none text-base text-vedic-textSecondary leading-relaxed space-y-4">
                    {content_html}
                </div>
            </section>'''
    
    html = re.sub(r'<article.*?</article>', f'<article class="flex-1 flex flex-col gap-16 pb-32">\n{article_content}\n</article>', html, flags=re.DOTALL)
    
    with codecs.open(f'app/static/{filename}', 'w', 'utf-8') as f:
        f.write(html)

hyperlink_content = '''
<h2 class="text-2xl font-bold text-vedic-forest mt-8 mb-4">1. Links to external websites/portals</h2>
<p>At many places in this website, you shall find links to other websites/portals. This links have been placed for your convenience. Ministry of AYUSH is not responsible for the contents and reliability of the linked websites and does not necessarily endorse the views expressed in them. Mere presence of the link or its listing on this website should not be assumed as endorsement of any kind. We cannot guarantee that these links will work all the time and we have no control over availability of linked pages.</p>

<h2 class="text-2xl font-bold text-vedic-forest mt-8 mb-4">2. Links to IP-SAKTI by other websites</h2>
<p>We do not object to you linking directly to the information that is hosted on this website and no prior permission is required for the same. However, we would like you to inform us about any links provided to this website so that you can be informed of any changes or updates therein. Also, we do not permit our pages to be loaded into frames on your site. The pages belonging to this website must load into a newly opened browser window of the User.</p>
'''

tkdl_content = '''
<h2 class="text-2xl font-bold text-vedic-forest mt-8 mb-4">CSIR-TKDL Access Protocol</h2>
<p>The Traditional Knowledge Digital Library (TKDL) is a pioneering Indian initiative to prevent misappropriation of country's traditional medicinal knowledge at International Patent Offices. Access to the full TKDL database is strictly regulated.</p>
<ul class="list-disc pl-5 space-y-2 mt-4">
    <li><strong>Sovereign Nodes:</strong> IP-SAKTI Sahayak interfaces with the TKDL database via a secure, 256-bit air-gapped sovereign node managed by the National Informatics Centre (NIC).</li>
    <li><strong>Non-Disclosure:</strong> By executing queries against the TKDL corpus, users agree not to export, publish, or disseminate the raw Shloka transcripts or exact translations for commercial use outside the scope of regulatory compliance.</li>
    <li><strong>Auditing:</strong> All queries matching TKDL Prior Art are logged in the sovereign registry to establish a permanent record of statutory evaluation.</li>
</ul>
<p class="mt-4">For full TKDL access, international patent examiners must rely on the existing Access Agreements signed with CSIR.</p>
'''

security_content = '''
<h2 class="text-2xl font-bold text-vedic-forest mt-8 mb-4">Security Architecture</h2>
<p>IP-SAKTI Sahayak operates within a highly secure framework mandated by the Government of India for managing sensitive Intellectual Property and Traditional Knowledge.</p>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
    <div class="p-6 border border-vedic-border rounded-lg bg-vedic-surface">
        <h3 class="font-bold text-vedic-forest mb-2">SHA-256 Verification</h3>
        <p class="text-sm">All backend transactions, classifications, and query logs are cryptographically signed using SHA-256 hashes to prevent tampering of regulatory records.</p>
    </div>
    <div class="p-6 border border-vedic-border rounded-lg bg-vedic-surface">
        <h3 class="font-bold text-vedic-forest mb-2">Zero-Hallucination Engine</h3>
        <p class="text-sm">The classification engine operates on a deterministic pipeline (Decision Tree) isolated from generative unpredictability, ensuring absolute statutory accuracy.</p>
    </div>
    <div class="p-6 border border-vedic-border rounded-lg bg-vedic-surface">
        <h3 class="font-bold text-vedic-forest mb-2">National SSO (Jan Parichay)</h3>
        <p class="text-sm">Identity management leverages MeriPehchan, the National Single Sign-On framework, bridging DigiLocker and Aadhar-based authentication.</p>
    </div>
    <div class="p-6 border border-vedic-border rounded-lg bg-vedic-surface">
        <h3 class="font-bold text-vedic-forest mb-2">NIC Cloud Hosting</h3>
        <p class="text-sm">The infrastructure is deployed entirely on the National Informatics Centre (NIC) sovereign cloud, maintaining data locality within Indian borders.</p>
    </div>
</div>
'''

make_page('hyperlink.html', 'Hyperlink Policy', hyperlink_content)
make_page('tkdl-nda.html', 'TKDL Non-Disclosure Registry', tkdl_content)
make_page('security-audit.html', 'Sovereign Security Audit', security_content)

print("Pages created successfully!")

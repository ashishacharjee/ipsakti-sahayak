// agent-bento-grid.js
class AgentBentoAnimations {
    constructor() {
        this.initClassifyBars();
        this.initFormFeed();
        this.initPipeline();
    }

    initClassifyBars() {
        const bars = document.querySelectorAll('.bento-bar');
        if (!bars.length) return;
        const heights = [[40, 75, 30, 80, 50], [70, 30, 85, 45, 90], [50, 90, 40, 75, 35]];
        let step = 0;
        setInterval(() => {
            bars.forEach((bar, i) => {
                bar.style.height = `${heights[i % 3][step % 5]}%`;
            });
            step++;
        }, 1500);
    }

    initFormFeed() {
        const els = document.querySelectorAll('.bento-feed-card');
        if (!els.length) return;
        
        let activeIdx = 0;
        
        const updateStack = () => {
            els.forEach((el, i) => {
                let diff = i - activeIdx;
                if (diff < 0) diff += els.length;
                
                if (diff === 0) {
                    el.style.transform = `translateY(0px) scale(1)`;
                    el.style.opacity = '1';
                    el.style.zIndex = '30';
                } else if (diff === 1) {
                    el.style.transform = `translateY(38px) scale(0.93)`;
                    el.style.opacity = '0.65';
                    el.style.zIndex = '20';
                } else if (diff === 2) {
                    el.style.transform = `translateY(68px) scale(0.86)`;
                    el.style.opacity = '0.38';
                    el.style.zIndex = '10';
                } else {
                    el.style.transform = `translateY(-38px) scale(0.93)`;
                    el.style.opacity = '0';
                    el.style.zIndex = '0';
                }
            });
            activeIdx = (activeIdx + 1) % els.length;
        };

        updateStack();
        setInterval(updateStack, 2000);
    }

    initPipeline() {
        const router = document.getElementById('bento-router-node');
        if (router) {
            let rot = 0;
            setInterval(() => {
                rot += 90;
                router.style.transform = `rotate(${rot}deg)`;
            }, 1500);
        }
        
        const beam = document.getElementById('bento-scan-beam');
        if (beam) {
            let pos = -100;
            setInterval(() => {
                pos = (pos > 200) ? -100 : pos + 15;
                beam.style.transform = `translateX(${pos}%)`;
            }, 50);
        }
    }
}
document.addEventListener('DOMContentLoaded', () => new AgentBentoAnimations());

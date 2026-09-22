const { useState, useEffect, useRef } = React;
const { motion, AnimatePresence } = window.Motion || window.FramerMotion || window.Motion; 

// If FramerMotion is loaded as window.Motion or window.FramerMotion
const MotionDiv = motion.div;
const MotionButton = motion.button;

// user profile changes if they are logged in or not (demo)
const isHub = window.location.pathname.includes('hub.html');

const user = {
    fullName: isHub ? "AYUSH Researcher" : "Guest Sandbox",
    email: isHub ? "researcher@ipsakti.gov.in" : "guest@ipsakti.gov.in",
    initials: isHub ? "AR" : "GS",
}

const contentAnimations = {
    initial: { opacity: 0, filter: "blur(8px)" },
    animate: { opacity: 1, filter: "blur(0px)", transition: { delay: 0.15 } },
    exit: { opacity: 0, filter: "blur(8px)" },
}

const SPRING = { type: "spring", bounce: 0.15, duration: 0.25 } // adjusted visualDuration to duration for older framer-motion compatibility

function Avatar({ large = false }) {
    return (
        <MotionDiv
            layoutId="clerk-avatar"
            transition={SPRING}
            className={large ? "user-btn__avatar--large" : "user-btn__avatar"}
        >
            {user.initials}
        </MotionDiv>
    )
}

function SecuredByClerk() {
    return (
        <a href="https://nic.in" target="_blank" rel="noreferrer" className="user-btn__clerk-credit">
            <span>Secured by</span>
            <span style={{ fontWeight: 'bold', color: '#1B4931', marginLeft: 4 }}>NIC Parichay</span>
        </a>
    )
}

function MenuItem({ children, onClick }) {
    return (
        <div className="user-btn__menu-item" onClick={onClick}>
            {children}
        </div>
    )
}

function MenuContent({ onManage, onSignOut }) {
    return (
        <MotionDiv
            layoutId="clerk-userbtn"
            className="user-btn__open"
            style={{ borderRadius: 16 }}
            transition={SPRING}
        >
            <div className="user-btn__menu-header">
                <div style={{ alignSelf: "center" }}>
                    <Avatar large />
                </div>
                <MotionDiv
                    className="user-btn__menu-header-content"
                    initial={contentAnimations.initial}
                    animate={contentAnimations.animate}
                    exit={contentAnimations.exit}
                >
                    <p>{user.fullName}</p>
                    <p>{user.email}</p>
                </MotionDiv>
            </div>
            <MotionDiv
                className="user-btn__menu-content"
                initial={contentAnimations.initial}
                animate={contentAnimations.animate}
                exit={contentAnimations.exit}
            >
                <MenuItem onClick={onManage}>
                    <svg fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fillRule="evenodd" clipRule="evenodd" d="M6.559 2.536A.667.667 0 0 1 7.212 2h1.574a.667.667 0 0 1 .653.536l.22 1.101c.466.178.9.429 1.287.744l1.065-.36a.667.667 0 0 1 .79.298l.787 1.362a.666.666 0 0 1-.136.834l-.845.742c.079.492.079.994 0 1.486l.845.742a.666.666 0 0 1 .137.833l-.787 1.363a.667.667 0 0 1-.791.298l-1.065-.36c-.386.315-.82.566-1.286.744l-.22 1.101a.666.666 0 0 1-.654.536H7.212a.666.666 0 0 1-.653-.536l-.22-1.101a4.664 4.664 0 0 1-1.287-.744l-1.065.36a.666.666 0 0 1-.79-.298L2.41 10.32a.667.667 0 0 1 .136-.834l.845-.743a4.7 4.7 0 0 1 0-1.485l-.845-.742a.667.667 0 0 1-.137-.833l.787-1.363a.667.667 0 0 1 .791-.298l1.065.36c.387-.315.821-.566 1.287-.744l.22-1.101ZM7.999 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z"></path></svg>
                    Manage Profile
                </MenuItem>
                <MenuItem onClick={onSignOut}>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill="currentColor" fillRule="evenodd" clipRule="evenodd" d="M2.6 2.604A2.045 2.045 0 0 1 4.052 2h3.417c.544 0 1.066.217 1.45.604.385.387.601.911.601 1.458v.69c0 .413-.334.75-.746.75a.748.748 0 0 1-.745-.75v-.69a.564.564 0 0 0-.56-.562H4.051a.558.558 0 0 0-.56.563v7.875a.564.564 0 0 0 .56.562h3.417a.558.558 0 0 0 .56-.563v-.671c0-.415.333-.75.745-.75s.746.335.746.75v.671c0 .548-.216 1.072-.6 1.459a2.045 2.045 0 0 1-1.45.604H4.05a2.045 2.045 0 0 1-1.45-.604A2.068 2.068 0 0 1 2 11.937V4.064c0-.548.216-1.072.6-1.459Zm8.386 3.116a.743.743 0 0 1 1.055 0l1.74 1.75a.753.753 0 0 1 0 1.06l-1.74 1.75a.743.743 0 0 1-1.055 0 .753.753 0 0 1 0-1.06l.467-.47H5.858A.748.748 0 0 1 5.112 8c0-.414.334-.75.746-.75h5.595l-.467-.47a.753.753 0 0 1 0-1.06Z"></path></svg>
                    {isHub ? "Sign Out" : "Sign In via Jan Parichay"}
                </MenuItem>
                <div style={{ marginTop: 4 }}>
                    <SecuredByClerk />
                </div>
            </MotionDiv>
        </MotionDiv>
    )
}

function UserButton() {
    const [open, setOpen] = useState(false)
    const rootRef = useRef(null)

    useEffect(() => {
        const handleKeyDown = (event) => {
            if (event.key === "Escape") setOpen(false)
        }
        window.addEventListener("keydown", handleKeyDown)
        return () => window.removeEventListener("keydown", handleKeyDown)
    }, [])

    useEffect(() => {
        if (!open) return
        const handleClickOutside = (event) => {
            if (rootRef.current && !rootRef.current.contains(event.target)) setOpen(false)
        }
        document.addEventListener("mousedown", handleClickOutside)
        return () => document.removeEventListener("mousedown", handleClickOutside)
    }, [open])

    return (
        <div className="user-btn__root" ref={rootRef}>
            <AnimatePresence>
                {!open ? (
                    <MotionButton
                        key="closed"
                        layoutId="clerk-userbtn"
                        className="user-btn__closed"
                        style={{ borderRadius: 99 }}
                        transition={SPRING}
                        onClick={() => setOpen(true)}
                        aria-label="Open account menu"
                    >
                        <Avatar />
                    </MotionButton>
                ) : (
                    <MenuContent
                        key="open"
                        onManage={() => setOpen(false)}
                        onSignOut={() => {
                            setOpen(false);
                            if (isHub) {
                                window.location.href = '/static/index.html';
                            } else {
                                window.location.href = '#jan-parichay-section';
                            }
                        }}
                    />
                )}
            </AnimatePresence>
        </div>
    )
}

function App() {
    return (
        <>
            <UserButton />
            <style>{`
                .user-btn__root { position: relative; width: 2rem; height: 2rem; }
                .user-btn__closed {
                    position: absolute; top: 0; left: 0; z-index: 90;
                    display: flex; align-items: center; justify-content: center;
                    width: 2rem; height: 2rem; padding: 0; border: 0; overflow: hidden;
                    cursor: pointer; background-color: var(--surface);
                    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
                }
                .user-btn__avatar, .user-btn__avatar--large {
                    display: flex; align-items: center; justify-content: center;
                    flex: none; width: 2rem; height: 2rem; border-radius: 99px;
                    background: #1B4931; /* Replaced Clerk purple with IP-SAKTI Green! */
                    color: #fff; font-size: 0.75rem; font-weight: 600; user-select: none;
                }
                .user-btn__avatar--large { width: 3rem; height: 3rem; font-size: 1rem; }
                .user-btn__open {
                    position: absolute; top: 0; right: 0; z-index: 90;
                    width: 216px; padding: 0.125rem; overflow: hidden;
                    background-color: #fff; border: 1px solid #e5e7eb;
                    box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
                    transform-origin: top right;
                }
                .dark .user-btn__open { background-color: #0e221b; border-color: #1a3c2f; color: #fff; }
                .dark .user-btn__menu-content { background-color: #0e221b; }
                .user-btn__menu-header { display: flex; flex-direction: column; gap: 0.75rem; padding: 1rem; }
                .user-btn__menu-header-content { text-align: center; align-self: center; }
                .user-btn__menu-header-content p:nth-child(1) { font-size: 0.875rem; font-weight: 500; margin: 0; }
                .user-btn__menu-header-content p:nth-child(2) { font-size: 0.75rem; opacity: 0.72; margin: 0; }
                .user-btn__menu-content { display: flex; flex-direction: column; gap: 0.125rem; padding: 0.25rem; }
                .user-btn__menu-item {
                    height: 2rem; display: flex; align-items: center; gap: 0.5rem;
                    padding: 0 0.75rem; user-select: none; font-size: 0.8125rem;
                    border-radius: 0.375rem; cursor: pointer; color: inherit;
                }
                .user-btn__menu-item:hover { background: rgba(0,0,0,0.05); }
                .dark .user-btn__menu-item:hover { background: rgba(255,255,255,0.05); }
                .user-btn__menu-item svg { width: 1rem; height: 1rem; }
                .user-btn__clerk-credit {
                    height: 2rem; display: flex; align-items: center; justify-content: center;
                    font-size: 0.75rem; color: #6b7280; text-decoration: none;
                }
            `}</style>
        </>
    )
}

const rootElement = document.getElementById("clerk-mount-point");
if (rootElement) {
    const root = ReactDOM.createRoot(rootElement);
    root.render(<App />);
}

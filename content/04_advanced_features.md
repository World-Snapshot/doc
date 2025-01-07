# Advanced Features

## Time Dimension Control Demo

<div id="demoContainer"></div>

<script type="text/babel">
const TimeControlParticles = () => {
    const [particles, setParticles] = React.useState([]);
    const [absoluteTime, setAbsoluteTime] = React.useState(50);
    const [relativeTime, setRelativeTime] = React.useState(50);
    const particleCount = 200;
    
    React.useEffect(() => {
        const initialParticles = Array.from({ length: particleCount }, (_, index) => {
            const gridSize = Math.ceil(Math.sqrt(particleCount));
            const row = Math.floor(index / gridSize);
            const col = index % gridSize;
            
            const x = (col / gridSize) * 100;
            const y = (row / gridSize) * 100;
            const angle = Math.random() * Math.PI * 2;
            const speed = 2 + Math.random() * 6;
            
            return {
                id: Math.random(),
                baseX: x,
                baseY: y,
                angle: angle,
                speed: speed,
                hue: Math.floor(Math.random() * 360),
                fullEndX: x + Math.cos(angle) * speed * 10,
                fullEndY: y + Math.sin(angle) * speed * 10,
            };
        });
        setParticles(initialParticles);
    }, []);

    const calculatePosition = (particle, absTime, relTime) => {
        const baseT = absTime / 100;
        const baseX = particle.baseX + (particle.fullEndX - particle.baseX) * baseT;
        const baseY = particle.baseY + (particle.fullEndY - particle.baseY) * baseT;

        const lineX = baseX;
        const lineY = baseY;

        const relativeOffset = ((relTime - 50) / 50) * 0.1;
        
        const currentX = baseX + Math.cos(particle.angle) * particle.speed * 10 * relativeOffset;
        const currentY = baseY + Math.sin(particle.angle) * particle.speed * 10 * relativeOffset;

        return {
            x: currentX,
            y: currentY,
            lineCenter: {
                x: lineX,
                y: lineY
            }
        };
    };

    return (
        <div className="w-full max-w-4xl p-4">
            <div className="bg-gray-900 rounded-lg p-6">
                <h2 className="text-2xl font-bold text-white mb-4">Laplace's Demon - Dual Time Dimension Controller</h2>
                
                <div className="relative h-96 bg-black rounded-lg overflow-hidden mb-4">
                    <div className="absolute inset-0">
                        {particles.map((particle) => {
                            const pos = calculatePosition(particle, absoluteTime, relativeTime);
                            
                            return (
                                <div key={particle.id} className="absolute" style={{
                                    width: '100%',
                                    height: '100%',
                                    pointerEvents: 'none'
                                }}>
                                    <div
                                        className="absolute"
                                        style={{
                                            backgroundColor: `hsla(${particle.hue}, 100%, 50%, 0.4)`,
                                            height: '2px',
                                            position: 'absolute',
                                            left: `${pos.lineCenter.x}%`,
                                            top: `${pos.lineCenter.y}%`,
                                            width: `${particle.speed * 2}%`,
                                            transform: `translate(-50%, -50%) rotate(${particle.angle}rad)`,
                                            transformOrigin: '50% 50%',
                                        }}
                                    />
                                    
                                    <div
                                        className="absolute rounded-full"
                                        style={{
                                            width: '4px',
                                            height: '4px',
                                            backgroundColor: `hsl(${particle.hue}, 100%, 70%)`,
                                            left: `${pos.x}%`,
                                            top: `${pos.y}%`,
                                            transform: 'translate(-50%, -50%)',
                                            boxShadow: `0 0 4px hsla(${particle.hue}, 100%, 70%, 0.8)`,
                                        }}
                                    />
                                </div>
                            );
                        })}
                    </div>
                </div>

                <div className="flex flex-col gap-2 mb-4">
                    <div className="text-white font-bold">Absolute Time (Global Time Flow)</div>
                    <div className="flex justify-between text-gray-300 text-sm">
                        <span>Past</span>
                        <span>Present</span>
                        <span>Future</span>
                    </div>
                    <input
                        type="range"
                        min="0"
                        max="100"
                        value={absoluteTime}
                        onChange={(e) => setAbsoluteTime(Number(e.target.value))}
                        className="w-full h-6"
                    />
                    <div className="text-gray-300 text-center">
                        Absolute Time Position: {absoluteTime}%
                    </div>
                </div>

                <div className="flex flex-col gap-2">
                    <div className="text-white font-bold">Relative Time (±10% Range)</div>
                    <div className="flex justify-between text-gray-300 text-sm">
                        <span>-10%</span>
                        <span>Current</span>
                        <span>+10%</span>
                    </div>
                    <input
                        type="range"
                        min="0"
                        max="100"
                        value={relativeTime}
                        onChange={(e) => setRelativeTime(Number(e.target.value))}
                        className="w-full h-6"
                    />
                    <div className="text-gray-300 text-center">
                        Relative Time Offset: {((relativeTime - 50) / 5).toFixed(1)}%
                    </div>
                </div>
            </div>
        </div>
    );
};

setTimeout(() => {
    const container = document.getElementById('demoContainer');
    if (container) {
        ReactDOM.render(<TimeControlParticles />, container);
    }
}, 100);
</script>

## About the Demo

This interactive visualization demonstrates our dual time dimension control system:

- **Absolute Time**: Controls the overall flow of time from past to future
- **Relative Time**: Allows fine-grained adjustment within a ±10% range around the current time point

The particles' movements and trajectories visualize how different time dimensions interact with each other in our system. Each particle represents a point in time-space, and its movement is influenced by both the absolute and relative time controls.
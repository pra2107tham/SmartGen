import React from 'react';
import { SparklesCore as Sparkle } from "@/components/ui/sparkles";
const SparklesCore = () => {
  return (
    <Sparkle
              id="tsparticlesfullpage"
              background="transparent"
              minSize={0.6}
              maxSize={1.4}
              particleDensity={20}
              className="w-full h-full"
              particleColor="#FFFFFF"
            />
  );
};

export default SparklesCore;

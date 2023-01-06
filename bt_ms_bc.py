from bluetooth import BluetoothListener, BluetoothEvent
from metasurface import Metasurface, ScatteringPattern
from brainwave_collector import BrainwaveCollector, AttentionIntensity

def main():
    # Set up the brainwave collector
    brainwave_collector = BrainwaveCollector()
    brainwave_collector.start()

    # Set up the Bluetooth listener
    bluetooth_listener = BluetoothListener()
    bluetooth_listener.start()

    # Set up the metasurface
    metasurface = Metasurface()

    # Map attention intensities to scattering patterns
    intensity_pattern_map = {
        AttentionIntensity.LOW: ScatteringPattern.DIFFUSE,
        AttentionIntensity.MEDIUM: ScatteringPattern.SPECULAR,
        AttentionIntensity.HIGH: ScatteringPattern.LASER,
    }

    # Listen for events from the brainwave collector and Bluetooth listener
    while True:
        event = select(brainwave_collector.events(), bluetooth_listener.events()).recv()

        if isinstance(event, BrainwaveEvent):
            # Find the corresponding scattering pattern for the attention intensity
            intensity = event.intensity
            scattering_pattern = intensity_pattern_map.get(intensity, ScatteringPattern.DIFFUSE)

            # Update the metasurface with the new scattering pattern
            metasurface.set_scattering_pattern(scattering_pattern)
        elif isinstance(event, BluetoothEvent):
            if event.type == BluetoothEvent.CONNECTION_ESTABLISHED:
                # Send the current scattering pattern to the connected device
                scattering_pattern = metasurface.scattering_pattern()
                bluetooth_listener.send(scattering_pattern)

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
from pl_mapper import run_pl_scan






def main():
    """
    Runs a batch of PL scans, showing each plot as it is completed.
    NOTE: You must close each plot window to proceed to the next scan.
    """
    # === DEFINE YOUR SCAN JOBS HERE ===
    scan_jobs = [
        {
            'center_x': 65, 'center_y': -370, 'center_f': -9.8,
            'x_size': 40, 'y_size': 40, 'step': 0.2,
            'comment': 'Flake K10'
        },
        {
            'center_x': 1120, 'center_y': -285, 'center_f': -17,
            'x_size': 40, 'y_size': 40, 'step': 0.2,
            'comment': 'Flake K13'
        },
    ]
    print(f"Starting batch of {len(scan_jobs)} PL scans...")

    for i, params in enumerate(scan_jobs):
        print(f"\n--- Running Scan Job {i+1}/{len(scan_jobs)} ({params.get('comment', 'No comment')}) ---")
        print(f"Parameters: {params}")
        
        try:
            # CHANGE #1: Call the scan function with show_plot=True
            # This will cause the plot to appear and pause the script.
            run_pl_scan(
                center_x=params['center_x'],
                center_y=params['center_y'],
                center_f=params['center_f'],
                x_size=params['x_size'],
                y_size=params['y_size'],
                step=params['step'],
                detector_config=2,
                show_plot=False
            )
        except Exception as e:
            print(f"!!! An error occurred during scan job {i+1}: {e} !!!")
            print("Continuing with the next job.")

    print("\nAll scan jobs are complete.")
    #Closing laser
    
    # CHANGE #2: The final plt.show() is removed because plots are shown individually.

if __name__ == '__main__':
    main()


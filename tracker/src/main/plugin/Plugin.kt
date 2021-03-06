package plugin

import plugin.activityTracker.TrackerLog
import plugin.activityTracker.liveplugin.openInEditor
import plugin.activityTracker.tracking.ActivityTracker
import com.intellij.ide.actions.RevealFileAction
import com.intellij.ide.util.PropertiesComponent
import com.intellij.openapi.project.Project

class Plugin(
    private val tracker: ActivityTracker,
    private val trackerLog: TrackerLog,
    private val propertiesComponent: PropertiesComponent
) {
    private var state: State = State.defaultValue
    private var pluginUI: PluginUI? = null

    fun init(): Plugin {
        state = State.load(propertiesComponent, pluginId)
        onStateChange(state)
        return this
    }

    fun setUI(pluginUI: PluginUI) {
        this.pluginUI = pluginUI
        pluginUI.update(state)
    }

    fun toggleTracking() = updateState { it.copy(codingModeIsTracking = !it.codingModeIsTracking) }

    fun openTrackingLogFile(project: Project?) {
        if (project == null) return
        openInEditor(trackerLog.currentLogFile().absolutePath, project)
    }

    fun openTrackingLogFolder() {
        RevealFileAction.openFile(trackerLog.currentLogFile().parentFile)
    }

    private fun updateState(closure: (State) -> State) {
        val oldState = state
        state = closure(state)
        if (oldState != state) {
            onStateChange(state)
        }
    }

    private fun onStateChange(newState: State) {
        tracker.stopTracking()
        if (newState.codingModeIsTracking) {
            tracker.startTracking(newState.toConfig())
        }
        pluginUI?.update(newState)
        newState.save(propertiesComponent, pluginId)
    }

    private fun State.toConfig() = ActivityTracker.Config(
        pollIdeState,
        pollIdeStateMs.toLong(),
        trackIdeActions,
        trackKeyboard,
        trackMouse,
        mouseMoveEventsThresholdMs.toLong()
    )


    data class State(
        var codingModeIsTracking: Boolean,
        val pollIdeState: Boolean,
        val pollIdeStateMs: Int,
        val trackIdeActions: Boolean,
        val trackKeyboard: Boolean,
        val trackMouse: Boolean,
        val mouseMoveEventsThresholdMs: Int
    ) {
        fun save(propertiesComponent: PropertiesComponent, id: String) {
            propertiesComponent.run {
                setValue("$id-isTracking", codingModeIsTracking, defaultValue.codingModeIsTracking)
                setValue("$id-pollIdeState", pollIdeState, defaultValue.pollIdeState)
                setValue("$id-pollIdeStateMs", pollIdeStateMs, defaultValue.pollIdeStateMs)
                setValue("$id-trackIdeActions", trackIdeActions, defaultValue.trackIdeActions)
                setValue("$id-trackKeyboard", trackKeyboard, defaultValue.trackKeyboard)
                setValue("$id-trackMouse", trackMouse, defaultValue.trackMouse)
                setValue("$id-mouseMoveEventsThresholdMs", mouseMoveEventsThresholdMs, defaultValue.mouseMoveEventsThresholdMs)
            }
        }

        companion object {
            val defaultValue = State(
                codingModeIsTracking = false,
                pollIdeState = true,
                pollIdeStateMs = 1000,
                trackIdeActions = true,
                trackKeyboard = false,
                trackMouse = false,
                mouseMoveEventsThresholdMs = 250
            )

            fun load(propertiesComponent: PropertiesComponent, id: String): State {
                return propertiesComponent.run {
                    State(
                        getBoolean("$id-isTracking", defaultValue.codingModeIsTracking),
                        getBoolean("$id-pollIdeState", defaultValue.pollIdeState),
                        getInt("$id-pollIdeStateMs", defaultValue.pollIdeStateMs),
                        getBoolean("$id-trackIdeActions", defaultValue.trackIdeActions),
                        getBoolean("$id-trackKeyboard", defaultValue.trackKeyboard),
                        getBoolean("$id-trackMouse", defaultValue.trackMouse),
                        getInt("$id-mouseMoveEventsThresholdMs", defaultValue.mouseMoveEventsThresholdMs)
                    )
                }
            }
        }
    }

    companion object {
        const val pluginId = "ActivityTracker"
    }
}